import asyncio
import time
import aiomysql

start = time.time()
async def read_data(table_name):
    conn = await aiomysql.connect(
        host="localhost",
        user="aref",
        password="EAsport1369",
        db="grafana"
    )
    async with conn.cursor() as cursor:
        await cursor.execute(f'select * from {table_name}')
        data = await cursor.fetchall()

async def main():
    conn = await aiomysql.connect(
        host="localhost",
        user="aref",
        password="EAsport1369",
        db="grafana"
    )

    async with conn.cursor() as cursor:
        await cursor.execute("show tables")
        tables = await cursor.fetchall()
        table_names = []
        for t in tables:
            table_names.append(t[0])

    tasks = []
    for t in table_names:
        tasks.append(asyncio.create_task(read_data(t)))

    await asyncio.gather(*tasks)
    end = time.time()
    print('Time Taken:',end-start)     
asyncio.run(main())
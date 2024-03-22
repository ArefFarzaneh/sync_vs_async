# MySQL Database Operations Comparison: Async vs Sync

This repository contains two versions of code for performing MySQL database operations using Python: asynchronous (asyncio) and synchronous. The purpose of this project is to compare the runtime performance of these two approaches and understand the advantages of asynchronous programming when dealing with database operations.

## Overview

In this project, we implement database operations such as reading data from multiple tables in a MySQL database. We provide two versions of the code:

1. **Async Version**: The asynchronous version of the code utilizes asyncio and aiomysql libraries to perform database operations concurrently, improving efficiency by leveraging non-blocking I/O.
2. **Sync Version**: The synchronous version of the code uses traditional synchronous programming techniques to perform database operations sequentially, without concurrency.

## Dependencies

Both versions of the code require the following dependencies:

- Python 3.7+
- aiomysql library (for async version)
- mysql-connector-python library (for sync version)

## Running the Code

To run the code and compare the runtime performance:

1. Clone this repository to your local machine.
2. Navigate to the repository directory.
3. Run the async version of the code:

    ```bash
    python async_version.py
    ```

4. Run the sync version of the code:

    ```bash
    python sync_version.py
    ```

5. Compare the runtime performance of both versions.

## Results and Observations

After running both versions of the code, analyze the runtime performance to observe the differences in execution time. Typically, you will notice that the async version completes database operations more quickly due to its ability to execute tasks concurrently, while the sync version processes operations sequentially.

## Contributing

Contributions to this project are welcome! If you have ideas for improvements or optimizations, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

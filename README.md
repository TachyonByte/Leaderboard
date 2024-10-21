
# Leaderboard Project

Capture the Flag (CTF) competitions are exciting events where teams compete by solving security challenges. The Leaderboard project acts as the heart of a CTF, allowing organizers to manage challenges, track team scores in real-time, and provide transparency to participants. This project is designed for both CTF organizers and participants to enhance the competition experience.

## Features

- Real-time leaderboard updates.
- User authentication and session management.
- Score submission and verification system.
- Easy-to-use admin interface for managing challenges and teams.
- Built-in security to prevent cheating or unauthorized score submissions.

## Technologies Used

- **Django**: A high-level Python Web framework.
- **Channels**: Enables handling WebSockets for real-time leaderboard updates.
- **Redis**: Used for caching and real-time communication.
- **Docker**: For containerizing the application.
- **Github Actions CI/CD**: Continuous integration and deployment pipelines.

## Installation

You can easily run the Leaderboard project using Docker. The project has been containerized and is available as an image on Docker Hub.

1. Pull the Docker image:

   ```bash
   docker pull tachyonbyte/leaderboard:latest
   ```

   Docker Hub link: [tachyonbyte/leaderboard](https://hub.docker.com/r/tachyonbyte/leaderboard)

2. Run the container:

   ```bash
   docker run -d -p 80:8089 tachyonbyte/leaderboard:latest
   ```

3. **(Optional) Implement persistence with volume mount:**

    To ensure data persistence, you can mount a volume for the SQLite database:

    ```bash
    docker run -d -p 80:8089 --mount source=sqlite-db,target=/app/ctf/ tachyonbyte/leaderboard:latest
    ```

    This command mounts the local `sqlite-db` volume to the container’s `/app/ctf/` directory, where the database is stored.

4. Access the leaderboard by visiting `http://localhost` in your browser.

## Usage

- Access the leaderboard and manage teams and challenges via the provided interface.
- Submit scores and track rankings in real-time.

## Contributing

Feel free to submit issues and pull requests to help improve the project.

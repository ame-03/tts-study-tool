import time

class LearningSession:
    def __init__(self, player, file_list, chunks):
        self.player = player
        self.file_list = file_list
        self.chunks = chunks

    def _print_progress(self, current, total, bar_length=20):
        progress = current / total
        filled = int(bar_length * progress)
        bar = "#" * filled + "-" * (bar_length - filled)
        print(f"\r[{bar}] {current}/{total}", end="", flush=True)

    def shadowing(self, pause=2.0):
        total = len(self.file_list)
        print("\n--- Shadowing Mode ---")
        print(f"Speed: {self.player.speed}x\n")
        try:
            for i, (file, text) in enumerate(zip(self.file_list, self.chunks), start=1):

                print(f"\nChunk {i}/{total}")
                print(f"Text: {text}")
                self._print_progress(i, total)
                print("\n▶ First play")
                self.player.play([file])
                print("⏸ Pause")
                time.sleep(pause)
                print("▶ Second play")
                self.player.play([file])
            print("\nDone.")

        except KeyboardInterrupt:
            print("\nStopped.")
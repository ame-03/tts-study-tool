import time
import os

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
    
    def repeat_mode(self, repeat_count=3, pause=1.5):
        total = len(self.file_list)
        print("\n--- Repeat Mode ---")
        print(f"Speed: {self.player.speed}x  |  Repeats: {repeat_count}x  |  Pause: {pause}s\n")
        try:
            for i, (file, text) in enumerate(zip(self.file_list, self.chunks), start=1):
                print(f"\nChunk {i}/{total}")
                print(f"Text: {text}")
                self._print_progress(i, total)
                for r in range(1, repeat_count + 1):
                    print(f"\n  ▶ Play {r}/{repeat_count}")
                    self.player.play([file])
                    if r < repeat_count:
                        time.sleep(pause)
            print("\nDone.")
        except KeyboardInterrupt:
            print("\nStopped.")
    
    def ab_repeat(self, start_index=None, end_index=None, repeat_count=3, pause=1.5):
        total = len(self.file_list)

        if start_index is None:
            self._list_chunks()
            try:
                start_index = int(input(f"Start(0-{total-1}): "))
                end_index   = int(input(f"End(0-{total-1}): "))
            except ValueError:
                print("Exeptipn input")
                return

        start_index = max(0, min(start_index, total - 1))
        end_index   = max(start_index, min(end_index, total - 1))

        target_files  = self.file_list[start_index : end_index + 1]
        target_chunks = self.chunks[start_index : end_index + 1]

        print(f"\n--- AB Repeat ---")
        print(f"Range: chunk {start_index} → {end_index}  |  {repeat_count}x  |  Speed: {self.player.speed}x\n")
        for chunk in target_chunks:
            print(f"  {chunk}")

        try:
            for r in range(1, repeat_count + 1):
                print(f"\n▶ Loop {r}/{repeat_count}")
                for j, (file, text) in enumerate(zip(target_files, target_chunks)):
                    print(f"  [{start_index + j}] {text}")
                    self.player.play([file])
                if r < repeat_count:
                    print(f"⏸ Pause {pause}s")
                    time.sleep(pause)
            print("\nDone.")
        except KeyboardInterrupt:
            print("\nStopped.")

    def save_script(self, output_path="data/scripts"):

        os.makedirs(output_path, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_path, f"script_{timestamp}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# TTS Study Script — {timestamp}\n\n")
            for i, chunk in enumerate(self.chunks):
                f.write(f"[{i:02d}] {chunk}\n")

        print(f"\n✓ Script saved: {filename}")
        return filename           
    
    
    def _list_chunks(self):
        print("\n--- Chunks ---")
        for i, chunk in enumerate(self.chunks):
            print(f"[{i}] {chunk}")
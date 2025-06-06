import argparse
from cic_gpt.namespace import NamespaceManager

def main():
    parser = argparse.ArgumentParser(description="CIC-GPT namespace manager")
    parser.add_argument("command", choices=["reset", "refresh", "continue", "diff"], help="Action to perform")
    parser.add_argument("--namespace", default="default", help="Namespace ID")
    args = parser.parse_args()

    ns = NamespaceManager(namespace_id=args.namespace)

    if args.command == "reset":
        ns.reset()
    elif args.command == "refresh":
        ns.refresh()
    elif args.command == "continue":
        ns.continue_session()
    elif args.command == "diff":
        ns.show_diff()

if __name__ == "__main__":
    main()

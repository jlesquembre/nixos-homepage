import click
import random
import toml

TEMPLATE = """
    <li>
      <a href="{url}">
        <img alt="{name}" src="{url}" />
        <h2>{name}</h2>
        {description}
      </a>
    </li>
"""

@click.command()
@click.option("--input", required=True, type=str)
def main(input):

    with open(input) as f:
        providers = toml.load(f)["commercial-provider"]

    random.shuffle(providers)

    for provider in providers:
        provider["name"] = provider["name"][:50]
        provider["description"] = provider["description"][:400]
        click.echo(TEMPLATE.format(**provider), nl=False)


if __name__ == "__main__":
    main()

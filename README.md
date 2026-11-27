<p align="center">
    <a href="https://github.com/KIRU-OP/Kirugram">
        <img
            src="https://raw.githubusercontent.com/kurigram-org/artwork/master/kurigram_logo_github.png"
            alt="Kirugram"
            height="128"
        />
    </a>
    <br />
    <b>Telegram MTProto API Framework for Python</b>
    <br />
    <a href="https://github.com/KIRU-OP/Kirugram"> Homepage </a>
    •
    <a href="https://github.com/KIRU-OP/Kirugram/issues"> Issues </a>
    <br />
    <br />
    <img
        src="https://img.shields.io/github/actions/workflow/status/KIRU-OP/Kirugram/python.yml?branch=main&logo=github&label=CI"
        alt="CI Tests"
    />
    <a href="https://github.com/KIRU-OP/Kirugram/blob/main/COPYING">
        <img
            src="https://img.shields.io/github/license/KIRU-OP/Kirugram.svg?color=%23fd5216"
            alt="License"
        />
    </a>
</p>


## Kirugram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

Kirugram is a community-maintained rebrand of Kurigram, itself derived from Pyrogram. It preserves upstream functionality while adopting the `kirugram` Python import namespace. Original authorship and license notices remain in place.

```python
from kirugram import Client\nfrom kirugram import filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Kirugram!")


app.run()
```

**Kirugram** is a modern, elegant and asynchronous [MTProto API](https://github.com/KIRU-OP/Kirugram/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Project lineage

Kirugram keeps the original upstream copyright notices and LGPL-3.0-or-later license. It is a community-maintained rebrand; it does not claim the original authorship of Pyrogram or Kurigram.

### Key Features

- **Ready**: Install Kirugram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [kuricrypt](https://github.com/kurigram-org/kuricrypt), a high-performance cryptography library written in Rust.
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

Stable version

``` bash
pip install kirugram
```

Dev version

``` bash
pip install https://github.com/KIRU-OP/Kirugram/archive/refs/heads/main.zip --force-reinstall
```

Optional dependencies

``` bash
pip install kirugram[fast]     # kuricrypt and uvloop for better performance
pip install kirugram[qrcode]   # QR code login support
```

### Resources

- Check out the [docs](https://github.com/KIRU-OP/Kirugram) to learn more about Kirugram, get started right
away and discover more in-depth material for building your client applications.
- Report bugs and request features through the [GitHub issue tracker](https://github.com/KIRU-OP/Kirugram/issues).

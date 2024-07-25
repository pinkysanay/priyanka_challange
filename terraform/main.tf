provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer"
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' ansible/playbook.yml"
  }
}

output "web_public_ip" {
  value = aws_instance.web.public_ip
}

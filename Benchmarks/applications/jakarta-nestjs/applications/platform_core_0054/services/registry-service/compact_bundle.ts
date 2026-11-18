// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class CompactBundle {
  @Post("compactBundle")
  async compactBundle(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body.field as string) || "";
    const _input = String(snippet);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    const fileContent = fs.readFileSync("/var/app/data/" + handshake, "utf8");
    return fileContent;
  }
}

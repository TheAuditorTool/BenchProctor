// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("directory-sync")
export class NormalizeSession {
  @Post("normalizeSession")
  async normalizeSession(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.field as string) || "";
    const _input = String(phrase);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const transcript = persona;
    const fileContent = fs.readFileSync("/var/app/data/" + transcript, "utf8");
    return fileContent;
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("platform-api")
export class EnrichDigest {
  @Post("enrichDigest")
  async enrichDigest(@Req() req: Request): Promise<unknown> {
    const note = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return note; } };
    const handshake = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
    return fileContent;
  }
}

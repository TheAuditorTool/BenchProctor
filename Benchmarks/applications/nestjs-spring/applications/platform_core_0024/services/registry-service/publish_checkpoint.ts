// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class PublishCheckpoint {
  @Post("publishCheckpoint")
  async publishCheckpoint(@Req() req: Request): Promise<unknown> {
    const heading = (req.body?.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("audit-log")
export class NormalizeFlag {
  @Post("normalizeFlag")
  async normalizeFlag(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: subtitle });
    const persona = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    fs.writeFileSync("/var/uploads/" + handshake, "data");
    return { created: true };
  }
}

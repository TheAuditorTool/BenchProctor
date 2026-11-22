// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("session-store")
export class NormalizeThreshold {
  @Post("normalizeThreshold")
  async normalizeThreshold(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: tagline });
    const persona = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const note = persona;
    fs.writeFileSync("/var/uploads/" + note, "data");
    return { created: true };
  }
}

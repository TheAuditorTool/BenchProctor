// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("audit-log")
export class BuildConfig {
  @Post("buildConfig")
  async buildConfig(@Req() req: Request): Promise<unknown> {
    const tagline = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(tagline);
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}

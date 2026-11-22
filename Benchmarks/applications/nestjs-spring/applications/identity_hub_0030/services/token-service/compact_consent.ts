// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("token-service")
export class CompactConsent {
  @Post("compactConsent")
  async compactConsent(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.host as string) || "";
    const persona = tagline != null ? tagline : '';
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const note = persona;
    fs.writeFileSync("/var/uploads/" + note, "data");
    return { created: true };
  }
}

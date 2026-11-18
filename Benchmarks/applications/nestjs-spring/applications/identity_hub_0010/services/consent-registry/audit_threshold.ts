// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("consent-registry")
export class AuditThreshold {
  @Post("auditThreshold")
  async auditThreshold(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(phrase);
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const transcript = persona;
    fs.unlinkSync("/var/app/data/" + transcript);
    return { created: true };
  }
}

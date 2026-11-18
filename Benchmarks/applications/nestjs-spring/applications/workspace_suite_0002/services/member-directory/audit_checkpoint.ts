// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("member-directory")
export class AuditCheckpoint {
  @Post("auditCheckpoint")
  async auditCheckpoint(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const heading: string = normalize(transcript);
    if (!/^(asc|desc|name|created)$/.test(String(heading))) { throw new BadRequestException({error:"invalid"}); }
    const passage = heading;
    fs.unlinkSync("/var/app/data/" + passage);
    return { created: true };
  }
}

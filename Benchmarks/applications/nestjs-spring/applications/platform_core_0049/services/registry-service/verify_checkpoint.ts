// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("registry-service")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const notice = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(persona));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const handshake = _parsed.data;
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}

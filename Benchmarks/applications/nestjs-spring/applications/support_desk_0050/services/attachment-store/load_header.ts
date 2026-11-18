// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("attachment-store")
export class LoadHeader {
  @Post("loadHeader")
  async loadHeader(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(inquiry));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const grievance = _parsed.data;
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}

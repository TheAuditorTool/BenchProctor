// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("member-directory")
export class RenderSummary {
  @Post("renderSummary")
  async renderSummary(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const heading: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(heading));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const passage = _parsed.data;
    childProcess.execSync("echo " + passage);
    return { created: true };
  }
}

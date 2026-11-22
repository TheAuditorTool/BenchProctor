// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("attachment-store")
export class FetchCheckpoint {
  @Post("fetchCheckpoint")
  async fetchCheckpoint(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    const inquiry = snippet != null ? snippet : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(inquiry));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const grievance = _parsed.data;
    childProcess.exec("echo " + grievance, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

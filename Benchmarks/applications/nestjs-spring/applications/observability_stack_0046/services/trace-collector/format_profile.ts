// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("trace-collector")
export class FormatProfile {
  @Post("formatProfile")
  async formatProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    const gauge = paragraph != null ? paragraph : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(gauge));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const cohort = _parsed.data;
    childProcess.exec("echo " + cohort, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

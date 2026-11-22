// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("metrics-ingest")
export class RotateThreshold {
  @Post("rotateThreshold")
  async rotateThreshold(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const cohort = excerpt != null ? excerpt : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(cohort));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const gauge = _parsed.data;
    childProcess.exec("echo " + gauge, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

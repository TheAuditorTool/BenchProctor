// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("presence-hub")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const _raw = remark;
    const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(synopsis));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const quotation = _parsed.data;
    childProcess.execSync("echo " + quotation);
    return { created: true };
  }
}

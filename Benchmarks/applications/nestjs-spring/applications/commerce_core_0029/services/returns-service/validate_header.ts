// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("returns-service")
export class ValidateHeader {
  @Post("validateHeader")
  async validateHeader(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["user-agent"] as string) || "";
    const backorder = notice != null ? notice : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(backorder));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const voucher = _parsed.data;
    childProcess.exec("echo " + voucher, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

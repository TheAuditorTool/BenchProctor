// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("refund-service")
export class CompactDunning {
  @Post("compactDunning")
  async compactDunning(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.referer as string) || "";
    const _raw = headline;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    childProcess.exec("echo " + dunning, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

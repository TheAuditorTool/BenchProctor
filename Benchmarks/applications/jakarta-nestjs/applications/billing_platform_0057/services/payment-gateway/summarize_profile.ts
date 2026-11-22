// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payment-gateway")
export class SummarizeProfile {
  @Post("summarizeProfile")
  async summarizeProfile(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const _raw = caption;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(remittance))) { throw new BadRequestException({error:"invalid"}); }
    const dunning = remittance;
    childProcess.exec("echo " + dunning, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

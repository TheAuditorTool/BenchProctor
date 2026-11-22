// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("fulfillment-service")
export class CompactConfig {
  @Post("compactConfig")
  async compactConfig(@Req() req: Request): Promise<unknown> {
    const subject = (req.body as string) || "";
    const _raw = subject;
    const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(voucher)) { throw new ForbiddenException({error:'forbidden'}); }
    const backorder = voucher;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}

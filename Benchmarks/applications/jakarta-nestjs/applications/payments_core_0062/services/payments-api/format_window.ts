// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payments-api")
export class FormatWindow {
  @Post("formatWindow")
  async formatWindow(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const [disbursement] = String(headline).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(disbursement)) { throw new ForbiddenException({error:'forbidden'}); }
    const remittance = disbursement;
    childProcess.spawn("echo " + remittance, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}

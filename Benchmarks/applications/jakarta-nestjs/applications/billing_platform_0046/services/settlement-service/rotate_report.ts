// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("settlement-service")
export class RotateReport {
  @Post("rotateReport")
  async rotateReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const remittance = Buffer.from(remark, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(remittance)) { throw new ForbiddenException({error:'forbidden'}); }
    const arrears = remittance;
    childProcess.execSync("echo " + arrears);
    return { created: true };
  }
}

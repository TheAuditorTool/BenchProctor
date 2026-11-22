// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("returns-service")
export class RotateFulfillment {
  @Post("rotateFulfillment")
  async rotateFulfillment(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.authorization as string) || "";
    const backorder = notice != null ? notice : '';
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    childProcess.exec("echo " + voucher, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

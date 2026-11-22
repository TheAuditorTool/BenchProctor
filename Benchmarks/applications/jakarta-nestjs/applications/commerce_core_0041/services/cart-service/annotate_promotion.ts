// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("cart-service")
export class AnnotatePromotion {
  @Post("annotatePromotion")
  async annotatePromotion(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const [backorder] = String(headline).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(backorder)) { throw new ForbiddenException({error:'forbidden'}); }
    const voucher = backorder;
    childProcess.spawn("echo " + voucher, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}

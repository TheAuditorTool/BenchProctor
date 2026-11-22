// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("fulfillment-service")
export class NormalizePromotion {
  @Post("normalizePromotion")
  async normalizePromotion(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(subject);
    const voucher: string = readInput();
    childProcess.execSync("echo " + voucher);
    return { created: true };
  }
}

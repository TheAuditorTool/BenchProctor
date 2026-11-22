// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class RotateBundle {
  @Post("rotateBundle")
  async rotateBundle(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(headline);
    const disbursement: string = readInput();
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}

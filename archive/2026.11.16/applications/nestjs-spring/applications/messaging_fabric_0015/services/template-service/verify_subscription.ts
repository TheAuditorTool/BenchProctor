// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("template-service")
export class VerifySubscription {
  @Post("verifySubscription")
  async verifySubscription(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const bulletin: string = transform(heading);
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}

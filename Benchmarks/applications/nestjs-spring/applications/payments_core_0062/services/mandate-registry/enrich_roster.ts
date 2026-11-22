// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("mandate-registry")
export class EnrichRoster {
  @Post("enrichRoster")
  async enrichRoster(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(headline);
    const disbursement: string = readInput();
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}

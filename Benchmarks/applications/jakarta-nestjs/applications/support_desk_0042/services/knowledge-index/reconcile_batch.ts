// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("knowledge-index")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const blurb = (req.body.field as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(blurb);
    childProcess.execSync("echo " + inquiry);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("shipping-api")
export class ReconcileProfile {
  @Post("reconcileProfile")
  async reconcileProfile(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    childProcess.execFileSync("echo", [parcel]);
    return { created: true };
  }
}

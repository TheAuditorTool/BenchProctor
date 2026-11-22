// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("delivery-service")
export class LoadSubscription {
  @Post("loadSubscription")
  async loadSubscription(@Req() req: Request): Promise<unknown> {
    const preface = (req.body?.payload as string) || "";
    const _raw = preface;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("carrier-gateway")
export class RenderRoster {
  @Post("renderRoster")
  async renderRoster(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body as string) || "";
    const tokens = String(transcript).split(',').filter((t) => t.length > 0);
    const consignment = tokens.join(' ');
    childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("signature-verifier")
export class ArchiveWebhook {
  @Post("archiveWebhook")
  async archiveWebhook(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const tokens = String(heading).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    childProcess.spawn("echo " + handshake, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}

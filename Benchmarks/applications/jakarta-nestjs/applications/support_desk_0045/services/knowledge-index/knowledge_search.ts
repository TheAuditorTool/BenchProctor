// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("knowledge-index")
export class SearchKnowledge {
  @Post("searchKnowledge")
  async searchKnowledge(@Req() req: Request): Promise<unknown> {
    const tagline = req.body.support_payload || "";
    childProcess.exec("echo " + tagline, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}

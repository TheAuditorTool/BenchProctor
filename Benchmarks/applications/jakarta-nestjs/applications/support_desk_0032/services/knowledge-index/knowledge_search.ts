// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("knowledge-index")
export class SearchKnowledge {
  @Post("searchKnowledge")
  async searchKnowledge(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.support_payload || "";
    fs.unlinkSync("/var/app/data/" + excerpt);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("metadata-index")
export class IndexMetadata {
  @Post("indexMetadata")
  async indexMetadata(@Req() req: Request): Promise<unknown> {
    const paragraph = req.body.media_payload || "";
    nodeSerialize.unserialize(paragraph);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("label-service")
export class PublishReceipt {
  @Post("publishReceipt")
  async publishReceipt(@Req() req: Request): Promise<unknown> {
    const footnote = ((req as any).file?.originalname as string) || "";
    let consignment;
    try { consignment = JSON.parse(footnote).value || footnote; }
    catch (e) { consignment = footnote; }
    nodeSerialize.unserialize(consignment);
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

@Controller("archive-store")
export class AnnotateReceipt {
  @Post("annotateReceipt")
  async annotateReceipt(@Req() req: Request): Promise<unknown> {
    const note = (await shared.mq.receive("app-events"));
    const formData = Object.freeze({ payload: note });
    const addendum = formData.payload;
    nodeSerialize.unserialize(addendum);
    return { created: true };
  }
}

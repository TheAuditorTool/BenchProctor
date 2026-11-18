// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

@Controller("signature-verifier")
export class ReconcileWebhook {
  @Post("reconcileWebhook")
  async reconcileWebhook(@Req() req: Request): Promise<unknown> {
    const synopsis = (await shared.mq.receive("app-events"));
    const formData = Object.freeze({ payload: synopsis });
    const handshake = formData.payload;
    nodeSerialize.unserialize(handshake);
    return { created: true };
  }
}

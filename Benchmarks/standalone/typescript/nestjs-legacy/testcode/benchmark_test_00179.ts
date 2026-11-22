// SPDX-License-Identifier: Apache-2.0
import { Controller, createParamDecorator, ExecutionContext, Post } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

const Cookies = createParamDecorator(
  (data: string, ctx: ExecutionContext): string => {
    const request = ctx.switchToHttp().getRequest();
    return request.cookies?.[data] ?? "";
  },
);
@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00179")
  async BenchmarkTest00179(@Cookies("session_token") cookieToken: string): Promise<unknown> {
    const userInput = cookieToken || "";
    const parts: string[] = [];
    for (const token of String(userInput).split(',')) { parts.push(token); }
    const data: string = parts.join(',');
    const streamKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
    const streamIv = crypto.randomBytes(12);
    const sealer = crypto.createCipheriv("aes-256-gcm", streamKey, streamIv);
    stream.pipeline(stream.Readable.from([String(data)]), sealer, fs.createWriteStream("/var/data/cipher.bin"), (err: Error | null) => { if (!err) fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([streamIv, sealer.getAuthTag()])); });
    return { created: true };
  }
}

// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
import * as crypto from "crypto";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

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
  @Post("BenchmarkTest00675")
  async BenchmarkTest00675(@Req() req: Request): Promise<unknown> {
    const userInput = ((req as any).rawBody as string) || "";
    const data = String(userInput).replace(/\u0000/g, "");
    crypto.createHash("md5").update(data).digest("hex");
    return { created: true };
  }
}

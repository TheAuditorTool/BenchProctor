// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00628")
  async BenchmarkTest00628(@Body("variables") vars: { input?: string }): Promise<unknown> {
    const userInput = (vars?.input as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    crypto.createHash("sha256").update(data).digest("hex");
    return { created: true };
  }
}

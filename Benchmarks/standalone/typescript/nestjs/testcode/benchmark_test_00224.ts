// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Redirect } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00224")
  @Redirect()
  async BenchmarkTest00224(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    return { url: data };
  }
}
